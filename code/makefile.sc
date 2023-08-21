CC := g++
CCFLAGS := -std=c++11 -O3 -lm -fopenmp
INC := -I src

.PRECIOUS : bin/%.o

VPATH = src/:main_sc/

SRC = $(notdir $(wildcard src/*.C))
OBJ = $(addprefix bin/, $(SRC:.C=.o))
HHH = $(wildcard src/*.h)

SRCSPROG := $(notdir $(wildcard main_sc/*.C))
EXE := $(addprefix bin/, $(SRCSPROG:.C=.exe))

all: allexe allobj

allexe: $(EXE)
allobj: $(OBJ)

bin/%.exe: bin/%.o $(OBJ)
	@echo "making executable $^... [$@]"
	$(CC) $(CCFLAGS) -o $@ $< $(INC) $(OBJ)

bin/%.o: %.C
	@echo "compiling $<... [$@]"
	$(CC) $(CCFLAGS) -c -o $@ $< $(INC)

clean:
	rm -fv bin/*.o bin/*.exe
