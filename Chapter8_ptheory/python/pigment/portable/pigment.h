struct _Pigment {
  char *name;
  char *filename;
  FILE *fp;
  char *units;
  int nBands;
  double *absorption;
  double *scaledAbsorption;
  double *wavelength;
  double concentration;
  double defaultConcentration;
  struct _Pigment *next;
};

typedef struct _Pigment Pigment;

char *DEFAULT_PIGS[] = {"CrefractiveIndex dummy 1 1 1","Cdm g/cm2 0.005 0.00001 0.01","Cab ug/cm2 40 0.00001 200","Cw  g/cm2 0.012 0.00001 0.01","Cs  arbitrary_unit 1 0 100"};
int DefaultNPIGS=4;
#define WHEREAMI "python/pigment/portable"


#ifndef MAX_STR
#define MAX_STR 128
#endif

#ifndef MAX
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#endif
