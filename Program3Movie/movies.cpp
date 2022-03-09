#include "movies.h"
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
  Movie::Movie(){
    title = "";
    director = "";
    rating = -1;
    genre = "";
    duration = -1;
    yearReleased = -1;
  }
  string Movie::getTitle(){
    return title;
  }
  void Movie::setTitle(string titles){
    title = titles;
  }
  string Movie::getDirector(){
    return director;
  }
  void Movie::setDirector(string dir){
    director = dir;
  }
  int Movie::getRating(){
    return rating;
  }
  void Movie::setRating(int num){
    rating = num;
  }
  string Movie::getGenre(){
    return genre;
  }
  void Movie::setGenre(string gen){
    genre = gen;
  }
  int Movie::getDuration(){
    return duration;
  }
  void Movie::setDuration(int i){
    duration = i;
  }
  int Movie::getYearReleased(){
    return yearReleased;
  }
  void Movie::setYearReleased(int release){
    yearReleased = release;
  }
  void Movie::setStars(vector<string> starList){
    stars.swap(starList);
  }
  vector<string> Movie::getStars(){
    return stars;
  }

  void Movie::print(){
      /*cout << cinema.getTitle() << " " << cinema.getDirector() << " " << cinema.getRating() << " " << cinema.getGenre() << " "<< cinema.getDuration() << " " << cinema.getYearReleased() << " " << cinema.getStars() << endl;*/
    cout << title << endl;
  }