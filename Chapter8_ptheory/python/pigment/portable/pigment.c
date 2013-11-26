#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "pigment.h"

/*double pow_dd(double a,double b){
	return(pow(a,b));
}*/

Pigment *allocatePig(Pigment *in){
  Pigment *out;
  if(!(out=(Pigment *)calloc(1,sizeof(Pigment)))){
    fprintf(stderr,"error in core allocation\n");
    exit(1);
  }
  if(in)in->next=out;
  return(out);
}

void deallocatePig(Pigment *pig,Pigment *prev){
  if(prev && prev->next==pig)prev->next=NULL;
  if(pig->name)free(pig->name);pig->name=NULL;
  if(pig->filename)free(pig->filename);pig->filename=NULL;
  if(pig->fp)fclose(pig->fp);pig->fp=NULL;
  if(pig->units)free(pig->units);pig->units=NULL;
  pig->nBands=0;
  if(pig->absorption)free(pig->absorption);pig->absorption=NULL;
  if(pig->scaledAbsorption)free(pig->scaledAbsorption);pig->scaledAbsorption=NULL;
  if(pig->wavelength)free(pig->wavelength);pig->wavelength=NULL;
  
  free(pig);
}

double *dcalloc(int n){
  double *out;
  if(!(out=(double *)calloc(n,sizeof(double)))){
    fprintf(stderr,"error in core allocation\n");
    exit(1);
  }
  return(out);
}

char *ccalloc(int n){
  char *out;
  if(!(out=(char *)calloc(n,sizeof(char)))){
    fprintf(stderr,"error in core allocation\n");
    exit(1);
  }
  return(out);
}


/*
** Function to read in a file from _where_
** of name _name_
** which has 2 columns: wavelength and spec. absorption
** in units _units_
** a reasonable default value _default_ and limits _max_ and _min_
**
** value returned is the pigment structure, linked in a linked list
** to _prev_
*/

Pigment *addPig(char *where,char *name,char *units,double ddefault,double max,double min,Pigment *prev){
  Pigment *pig;
  double d1,d2;
  int i;

  if(!name || name[0] != 'C'){
    fprintf(stderr,"error in addPig: no name specified\nor name does not begin with 'C' (e.g. Cab)");
    return(NULL);
  }
  pig=allocatePig(prev);

  pig->name=ccalloc(strlen(name)+1);
  strcpy(pig->name,name);
  name[0]='k';
  pig->filename=ccalloc(strlen(name)+strlen(where)+strlen("/.dat")+1);
  sprintf(pig->filename,"%s/%s.dat",where,name);
  if(!(pig->fp=(FILE *)fopen(pig->filename,"r"))){
    fprintf(stderr,"ERROR opening pigment file %s\n",pig->filename);
    deallocatePig(pig,prev);
    return(NULL);
  }
  pig->nBands=0;
  while(fscanf(pig->fp,"%lf %lf",&d1,&d2)==2)pig->nBands++;
  rewind(pig->fp);
  pig->absorption=dcalloc(pig->nBands);
  pig->scaledAbsorption=dcalloc(pig->nBands);
  pig->wavelength=dcalloc(pig->nBands);
  pig->defaultConcentration=pig->concentration=MAX(min,MIN(max,ddefault));
  i=0;
  while(fscanf(pig->fp,"%lf %lf",&d1,&d2)==2){
    pig->wavelength[i]=d1;
    pig->absorption[i]=d2;
    pig->scaledAbsorption[i]=d2*pig->concentration;
    i++;
  }
  fclose(pig->fp);
  return(pig);
}

int setConcentration(Pigment *pig,double conc){
  int i;
  if(!(pig->nBands)){
    fprintf(stderr,"FATAL: no data read in to pigment\n");
    deallocatePig(pig,NULL);
    return(0);
  }
  pig->concentration=conc;
  for(i=0;i<pig->nBands;i++){
    pig->scaledAbsorption[i]=pig->absorption[i]*pig->concentration;
  }
  return(1);
}

double getAbsorption(double wavelength,Pigment *pig){
  int i;
  double out=0.,diff;
  if(wavelength<pig->wavelength[0]||wavelength>pig->wavelength[pig->nBands-1])
    out=0;
  else for(i=0;i<pig->nBands-1;i++){
    if(wavelength>=pig->wavelength[i]&&wavelength<=pig->wavelength[i+1]){
      diff=(wavelength-pig->wavelength[i])/(pig->wavelength[i+1]-pig->wavelength[i]);
      out=pig->scaledAbsorption[i]+diff*(pig->scaledAbsorption[i+1]-pig->scaledAbsorption[i]);
      return(out);
    }
  }
  return(0.);
}

int totalAbsorptions(double *wavelength,double *data,int nBands,Pigment *start,double vai){
  int i;
  double absorb;
  Pigment *goon;
  if(!data){
    data=dcalloc(nBands);
  }
  for(i=0;i<nBands;i++){
    goon=start;
    absorb=0;
    while(goon){
      absorb+=getAbsorption(wavelength[i],goon);
      goon=goon->next;
    }
    data[i]=absorb/vai;
  }
  return(1);

}

Pigment *initiate(Pigment **start){
  int i,addThis=0;
  char name[MAX_STR],unit[MAX_STR];
  double defaultConc,min,max;
  Pigment *this=NULL,*old=NULL;

  for(i=0;i<DefaultNPIGS;i++){
    sscanf(DEFAULT_PIGS[i],"%s %s %lf %lf %lf",name,unit,&defaultConc,&min,&max);
    this=addPig(WHEREAMI,name,unit,defaultConc,max,min,old);
    if(i==0)*start=this;
    old=this;
  }
  /* now scan the stdin for any additional information or overrides */
  while(fscanf(stdin,"%s %s %lf %lf %lf",name,unit,&defaultConc,&min,&max)==5){
    addThis=1;
    /* check to see if it exists */
    {
      Pigment *_old,*_this;
      _old=NULL;
      _this=*start;
      while(_this){
	if(!strcmp(_this->name,name)){
	  /* override */
	  if(_this->units)free(_this->units);
	  _this->units=ccalloc(strlen(unit)+1);
	  strcpy(_this->units,unit);
	  setConcentration(_this,MIN(max,MAX(min,defaultConc)));
	  addThis=0;
	  _this=NULL;
	}else{
	  _old=_this;
	  _this=_this->next;
	}
      }
    }
    if(addThis){
      this=addPig(WHEREAMI,name,unit,defaultConc,max,min,old);
      old=this;
    }
  }
}


int main(int argc,char **argv){
  Pigment *start=NULL,*refractiveIndex;
  double lStart=400,lEnd=2400,lD=5,*wavelength,*data,di,atof(const char *);
  int i,nBands=0;

  double N=1.0,refl[1],trans[1],n,k;

  /* read N */
  for(i=1;i<argc;i++){
    if(!(strcmp("-N",argv[i]))){
      sscanf(argv[i+1],"%lf",&N);
      i++;
    }else if(!(strcmp("-l",argv[i]))){
      lStart=atof(argv[++i]);
      lEnd=atof(argv[++i]);
      lD=atof(argv[++i]);
    }
  }

  initiate(&refractiveIndex);
  start=refractiveIndex->next;

  for(di=lStart;di<=lEnd;di+=lD)nBands++;
  wavelength=dcalloc(nBands);
  for(di=lStart,i=0;di<=lEnd;i++,di+=lD)wavelength[i]=di;
  data=dcalloc(nBands);

  totalAbsorptions(wavelength,data,nBands,start,N);
  for(di=lStart,i=0;di<=lEnd;i++,di+=lD){
    /* get the refractive index (the first element in linked list */
    n=getAbsorption(wavelength[i],refractiveIndex);
    k=data[i];
    /* call to prospect code */
    leaf_(refl,trans,&N,&n,&k);
    fprintf(stdout,"%lf %lf %lf %lf\n",wavelength[i],refl[0],trans[0],data[i]);
  }
  return(0);
}
