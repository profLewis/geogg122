CFLAGS = -g
#CFLAGS = -O -Bstatic
#LIBS = -lc -lF77 -lsunmath -lm #
#LIBS = -lc -lF77 -lsunmath -lm #
LIBS = -lc -lm 
INCLS = -I/usr/local/include
INCLS += -I/usr/include
FF = gfortran
CC = gcc
OUT = pigment



$(OUT):		pigment.o prospect.redux.o
		${FF} ${CFLAGS} ${INCLS} prospect.redux.o pigment.o -o ${OUT} ${LIBS}

.c.o:	makefile $<
		$(CC) $(CFLAGS) -c $<

.f.o:	makefile $<
		$(FF) $(CFLAGS) -c $<

clean:
		\rm -f *.o *~ *%

install:
		cp pigment ../../../bin/pigment

test:		pigment
		pigment -l 400 2400 1 -N 1 < defaults.dat > test_result.dat
		diff test_result.dat result.dat



