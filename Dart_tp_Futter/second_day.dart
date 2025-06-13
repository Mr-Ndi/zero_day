class Animal {
  String name;
  Animal(this.name);
  void speak()
  {
    print('$name makes sounds');
  }
}
void main()
{
  var sample = Animal('cows');
  sample.speak();
}
