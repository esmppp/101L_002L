#include <iostream>
#include <iomanip>
//#include <cctype>
//#include <cstring>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include "functions.h"
using namespace std;
char menu(){
  char tempChoice;
  cout << "MENU CHOICES" << endl;
  cout << "M - Print Movies List" << endl;
  cout << "S - Print Stars for a Given Movie" << endl;
  cout << "F - Find the Movie the Star is in" << endl;
  cout << "Q - Quit" << endl;
  cout << endl;
  cout << "Enter your choice: ";
  cin >> tempChoice;
  cout << "***" << tempChoice << endl;
  tempChoice = toupper(tempChoice);
  return tempChoice;
}

int readInFile(vector<Movie>& cinema,ifstream& inFile, ofstream& outFile){
    string inRec, tempString;
    vector<string> temp, tempStars;
    Movie tempFilm;
    int tempRating, tempDur, tempYear;
    while(getline(inFile,inRec)){
      stringstream inSS(inRec);
      temp.clear();
      while(getline(inSS,tempString,',')){
        temp.push_back(tempString);
      }
      if(temp[0] == "M"){
        try{
          //3 5 6
          tempRating = stoi(temp[3]);
          tempDur = stoi(temp[5]);
          tempYear = stoi(temp[6]);
          tempStars.clear();
          for(int i = 7; i < temp.size(); i++){
            tempStars.push_back(temp[i]);
          }
        }catch(...){
          outFile << "ERROR: " << inRec << endl;
          outFile << "Previous line had stoi error" << endl;
          continue;
        }
        tempFilm.setTitle(temp[1]);
        tempFilm.setDirector(temp[2]);
        tempFilm.setRating(tempRating);
        tempFilm.setGenre(temp[4]);
        tempFilm.setDuration(tempDur);
        tempFilm.setYearReleased(tempYear);
        tempFilm.setStars(tempStars);
        cinema.push_back(tempFilm);
      }
    }
  }