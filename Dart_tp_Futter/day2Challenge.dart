class Vehicle{
  String vehicle;

Vehicle(this.vehicle);
  void drive(){
    print('$vehicle will take you anywhere');
  }
}

class Bike extends Vehicle{
  Bike(String vehicle): super(vehicle);
}

class Car extends Vehicle{
  Car(String vehicle): super(vehicle);
}

mixin Flying {
  void flyin() => print('Today I go fly');
}
class Bird with Flying{}

class Student{
  //Map for storing marks
  Map<String, double>Marks = {'herve':9.5, 'Mbaduko': 9.5, 'Ndi': 9.5};
  
  void display(){
    print(Marks);
  }
}

void main() {
  var question1_1 = Vehicle('Volkswagern');
  var question1_2 = Bike('Matabaro');
  var question1_3 = Car('Yamaha');

  var question2 = Bird();

  var question3 = Student();


  question1_1.drive();
  question1_2.drive();
  question1_3.drive();
  print('-----------------------------------------------------------------------------');
  question2.flyin();

  print('-----------------------------------------------------------------------------');
  question3.display();
}
