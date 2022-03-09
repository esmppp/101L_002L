#pragma once
#include <string>
#include <vector>

using namespace std;
class Movie{
public:
  //NO PRE OR POSTS FOR GETTERS OR SETTERS
  Movie();
  string getTitle();
  void setTitle(string titles);
  string getDirector();
  void setDirector(string dir);
  int getRating();
  void setRating(int num);
  string getGenre();
  void setGenre(string gen);
  int getDuration();
  void setDuration(int i);
  int getYearReleased();
  void setYearReleased(int release);

  void setStars(vector<string> starList);
  vector<string> getStars();
  void print();
  //pre:
  //post:

private:
  string title;
  string director;
  int rating;
  string genre;
  int duration;
  int yearReleased;
  vector<string> stars;
};