all: algo.ex stat.ex

algo.ex: source/algo.sh
	cp source/algo.sh algo.ex
	chmod +x algo.ex	

stat.ex: source/stat.sh
	cp source/stat.sh stat.ex
	chmod +x stat.ex
