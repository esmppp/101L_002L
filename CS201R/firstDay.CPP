#include <iostream> // Lets it work with input and output

using namespace std;
int main() // The main function. Everything in python is a function
{
  string name, name2;
  cout << "Please enter your name: \n";
  cin >> name; //cin is standard input file, your keyboard
  cin >> name2;
  // If cin finds a space, it will stop there and not take any part of the string afterwards.
  cout << "Hello "<< name << "!\n";
  // using namespace std lets you write just cout instead of std::cout on line 6
}

// count++ and ++count are two DIFFERENT THINGS. They change the variable at different spots. Same with --. If its before, it changes before being assigned, if its after then it will get assigned then update anything.