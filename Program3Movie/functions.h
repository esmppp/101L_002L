#pragma once
#include <string>
#include "movies.h"
using namespace std;

char menu();
//pre:Takes in no variables
//post: prints out menu options and returns selected option

int readInFile(vector<Movie>& cinema, ifstream& inFile, ofstream& outFile);
  //pre: takes in empty movie vector, an input stream, and an output stream
  //post: adds all non-errored input from file to vector, and sends all errors to output file