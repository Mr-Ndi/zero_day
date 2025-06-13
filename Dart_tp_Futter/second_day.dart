class Animal {
  String name;
  Animal(this.name);
  void speak()
  {
    print('$name makes sounds');
  }
}
class Dog extends Animal{
  Dog(String name): super(name);

  void speak() {
    print('$name make sounds');
  }
}
void main()
{
  var sample = Animal('cows');
  var sample2 = Dog('kamazage');
  sample.speak();
  sample2.speak();
}
