.PHONY: clean

coll_finder: md5.o main.o
	g++ $^ -o $@ -Llib -lcoll

lib/libcoll.a:
	cd lib && $(MAKE)

clean:
	rm -f coll_finder
	rm -f *.o
	cd lib && $(MAKE) clean
