.PHONY: all clean install uninstall

all: Nikitatest

clean:
	rm -rf Nikitatest *.o
main.o: main.c
	gcc -c -o main.o main.c
Nikitatest: main.o
	gcc -o Nikitatest main.o


dist: Nikitatest-1.0.tar.gz
Nikitatest-1.0.tar.gz: Nikitatest
	rm -rf Nikitatest-1.0
	mkdir Nikitatest-1.0
	cp *.c Makefile Nikitatest-1.0
	tar zcvf $@ Nikitatest-1.0
