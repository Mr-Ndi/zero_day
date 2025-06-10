import 'dart:io';

main(){
 //  stdout.writeln('What is your name: ?');
//String name = stdin.readLineSync()!;
//  print('My name is $name');
print('Hello by using space as the separator can u eneter the element of your list pls');
String input = stdin.readLineSync()!;
List<String> String_numbers = input.split(' ');
List<int> number = String_numbers.map(int.parse).toList();
List<int> even = [];
print('I guese that this is your input: $number');

for (var num in number){
  if (num % 2 == 0){
    even.add(num);
  }
}
print('Among the enetered number here is even one among them: $even');
}
