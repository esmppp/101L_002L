#include <iostream>
#include <vector>
#include <fstream>
#include "functions.h"
#include "movies.h"

int main() {
  vector<Movie> movieList;
  ifstream inFile;
  ofstream outFile;
  inFile.open("movieList.csv");
  outFile.open("outfile.txt");
  if(!inFile.is_open() || !outFile.is_open()){
    cout << "ERROR: FILE NOT FOUND" << endl;
    return 1;
  }

  readInFile(movieList,inFile,outFile);
  for(int i = 0; i < movieList.size(); i++){
    movieList[i].print();
  }
  
  /*char option = menu();
  while(option != 'Q'){
    if(option == 'M'){
      //stuff
    }else if(option == 'S'){
      //other stuff
    }else if(option == 'F'){
      //more stuff
    }
    option = menu();
  }*/
  return 0;
}