class Animal {
  String name;
  Animal(this.name);
  void speak()
  {
    print('$name makes sounds');
  }
}

//---------------------------------------------------------------------------------------------------
class Dog extends Animal{
  Dog(String name): super(name);

  void speak() {
    print('$name make sounds');
  }
}

//---------------------------------------------------------------------------------------------------
mixin Fly {
  void flying() => print('Flyin, ...');
}

mixin Swimming{
  void swimming() => print('Swimming, ...');
}

class Duck with Fly, Swimming{}
//---------------------------------------------------------------------------------------------------
void main()
{
  //var sample = Animal('cows');
  //var sample2 = Dog('kamazage');
  //var sampleDuck = Duck();


  //sample.speak();
  //sample2.speak();
  //sampleDuck.flying();
  //sampleDuck.swimming();
  //List
  List<String> fruits=['Apple','Banana','Orange'];
  fruits.add('Grapes');
  print(fruits);

  // Map
  Map<String, int> scores = {'Alice': 90, 'Bob': 85};
  scores['Charlie'] = 88;
  print(scores);

  // Set
  Set<int> uniqueNumbers = {1, 2, 3, 3, 4};
  uniqueNumbers.add(5);
  print(uniqueNumbers); // {1, 2, 3, 4, 5}
}
