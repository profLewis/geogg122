c     ******************************************************************
c     Jacquemoud S., Ustin S.L., Verdebout J., Schmuck G., Andreoli G.,
c     Hosgood B. (1995), PROSPECT return, Remote Sens, Environ., in
c     preparation.
c     Jacquemoud S., Baret F. (1990), PROSPECT: a model of leaf optical
c     properties spectra, Remote Sens. Environ., 34:75-91.
c     ******************************************************************
c     Stephane JACQUEMOUD
c     University of California, Davis
c     Department of Land, Air, and Water Resources
c     Davis, CA 95616
c     USA
c     tel: (1)-916-752-5092
c     fax: (1)-916-752-5262
c     E-mail: stephane@vache.ucdavis.edu
c     Mosaic: http://vaca.ucdavis.edu/staff/stephane/index.html
c     version 2.01 (10 April 1995)
c     ******************************************************************
c     
c     
c    Modified to be passed array with the absn in
c    Lewis Jan 3 2004
c     


      subroutine leaf(main_r,main_t,vai,n,k)

      double precision vai,n,k
      double precision refl,main_r(1),main_t(1),tran
      double precision inex
      double precision teta,tau
      double precision t1,t2,x1,x2,x3,x4,x5,x6,r,t,ra,ta
      double precision delta,alfa,beta,va,vb,s1,s2,s3

      intrinsic sqrt,exp

      common /leafout/refl,tran
      common /nagout/inex
      common /tauin/teta
      common /tauout/tau

c     ******************************************************************
c     reflectance and transmittance of one layer
c     ******************************************************************
c     Allen W.A., Gausman H.W., Richardson A.J., Thomas J.R. (1969),
c     Interaction of isotropic ligth with a compact plant leaf, J. Opt.
c     Soc. Am., 59(10):1376-1379.
c     Jacquemoud S., Baret F. (1990), Prospect: a model of leaf optical
c     properties spectra, Remote Sens. Environ., 34:75-91.
c     ******************************************************************

      i=1

      if (k.le.0.) then
        k=1.
      else
        call s13aaf(vai,n,k)

        k=(1.-k)*dexp(-k)+k**2*inex
      endif

      teta=90.
      call tav(vai,n)
      t1=tau
      teta=60.
      call tav(vai,n)
      t2=tau
      x1=1.-t1
      x2=t1**2*k**2*(n**2-t1)
      x3=t1**2*k*n**2
      x4=n**4-k**2*(n**2-t1)**2
      x5=t2/t1
      x6=x5*(t1-1.)+1.-t2
      r=x1+x2/x4
      t=x3/x4
      ra=x5*r+x6
      ta=x5*t

c     ******************************************************************
c     reflectance and transmittance of N layers
c     ******************************************************************
c     Stokes G.G. (1862), On the intensity of the light reflected from
c     or transmitted through a pile of plates, Proc. Roy. Soc. Lond.,
c     11:545-556.
c     ******************************************************************

      delta=(t**2-r**2-1.)**2-4.*r**2
      alfa=(1.+r**2-t**2+dsqrt(delta))/(2.*r)
      beta=(1.+r**2-t**2-dsqrt(delta))/(2.*r)
      va=(1.+r**2-t**2+dsqrt(delta))/(2.*r)
      vb=dsqrt(beta*(alfa-r)/(alfa*(beta-r)))
      s1=ra*(va*vb**(vai-1.)-va**(-1.)*vb**(-(vai-1.)))
     &   +(ta*t-ra*r)*(vb**(vai-1.)-vb**(-(vai-1.)))
      s2=ta*(va-va**(-1.))
      s3=va*vb**(vai-1.)-va**(-1.)*vb**(-(vai-1.))
     &   -r*(vb**(vai-1.)-vb**(-(vai-1.)))
      refl=s1/s3
      tran=s2/s3
      main_r(i)=refl
      main_t(i)=tran
      return
      end

c     ******************************************************************
c     exponential integral: int(exp(-t)/t,t=x..inf)
c     ******************************************************************

      subroutine s13aaf(vai,n,k)

      double precision vai,n,k
      double precision inex,x,y

      intrinsic log,exp

      common /nagout/inex

      if (k.gt.4.) goto 10

      x=0.5*k-1.
      y=(((((((((((((((-3.60311230482612224d-13
     &  *x+3.46348526554087424d-12)*x-2.99627399604128973d-11)
     &  *x+2.57747807106988589d-10)*x-2.09330568435488303d-9)
     &  *x+1.59501329936987818d-8)*x-1.13717900285428895d-7)
     &  *x+7.55292885309152956d-7)*x-4.64980751480619431d-6)
     &  *x+2.63830365675408129d-5)*x-1.37089870978830576d-4)
     &  *x+6.47686503728103400d-4)*x-2.76060141343627983d-3)
     &  *x+1.05306034687449505d-2)*x-3.57191348753631956d-2)
     &  *x+1.07774527938978692d-1)*x-2.96997075145080963d-1
      y=(y*x+8.64664716763387311d-1)*x+7.42047691268006429d-1
      inex=y-dlog(k)
      goto 30

10    if (k.ge.85.) goto 20
      x=14.5/(k+3.25)-1.
      y=(((((((((((((((-1.62806570868460749d-12
     &  *x-8.95400579318284288d-13)*x-4.08352702838151578d-12)
     &  *x-1.45132988248537498d-11)*x-8.35086918940757852d-11)
     &  *x-2.13638678953766289d-10)*x-1.10302431467069770d-9)
     &  *x-3.67128915633455484d-9)*x-1.66980544304104726d-8)
     &  *x-6.11774386401295125d-8)*x-2.70306163610271497d-7)
     &  *x-1.05565006992891261d-6)*x-4.72090467203711484d-6)
     &  *x-1.95076375089955937d-5)*x-9.16450482931221453d-5)
     &  *x-4.05892130452128677d-4)*x-2.14213055000334718d-3
      y=((y*x-1.06374875116569657d-2)*x-8.50699154984571871d-2)*x
     &  +9.23755307807784058d-1
      inex=dexp(-k)*y/k
      goto 30

20    inex=0.
      goto 30

30    continue

      return
      end

c     ******************************************************************
c     evaluation of tav for any solid angle
c     ******************************************************************
c     Stern F. (1964), Transmission of isotropic radiation across an
c     interface between two dielectrics, Appl. Opt., 3(1):111-113.
c     Allen W.A. (1973), Transmission of isotropic light across a
c     dielectric surface in two and three dimensions, J. Opt. Soc. Am.,
c     63(6):664-666.
c     ******************************************************************

      subroutine tav(vai,n)

      double precision pi,rd
      double precision vai,n
      double precision teta,tau
      double precision r2,rp,rm,a,b,ds
      double precision b0,b1,b2,ts,tp1,tp2,tp3,tp4,tp5,tp

      intrinsic sqrt,log,sin

      common /tauin/teta
      common /tauout/tau

      pi=dacos(0.d+0)*2.
      rd=pi/180.

      teta=teta*rd
      r2=n**2
      rp=r2+1.
      rm=r2-1.
      a=(n+1.)**2/2.
      b=-(r2-1.)**2/4.
      ds=dsin(teta)

      if (teta.eq.0.) then
        tau=4.*n/(n+1.)**2
      else
        if (teta.eq.pi/2.) then
          b1=0.
        else
          b1=dsqrt((ds**2-rp/2.)**2+b)
        endif
        b2=ds**2-rp/2.
        b0=b1-b2
        ts=(b**2/(6.*b0**3)+b/b0-b0/2.)-(b**2/(6.*a**3)+b/a-a/2.)
        tp1=-2.*r2*(b0-a)/rp**2
        tp2=-2.*r2*rp*dlog(b0/a)/rm**2
        tp3=r2*(1./b0-1./a)/2.
        tp4=16.*r2**2*(r2**2+1.)*dlog((2.*rp*b0-rm**2)/(2.*rp*a-rm**2))
     &      /(rp**3*rm**2)
        tp5=16.*r2**3*(1./(2.*rp*b0-rm**2)-1./(2.*rp*a-rm**2))/rp**3
        tp=tp1+tp2+tp3+tp4+tp5
        tau=(ts+tp)/(2.*ds**2)
      endif

      return
      end

