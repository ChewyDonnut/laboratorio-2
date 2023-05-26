
import 'dart:io';
import 'dart:math';

void main(){
var random=Random();
List<int>lista=[14,2,5,3,9];
List<int>lista2=[];
List<int>lista3=[];
for(int i=0;i<5;i++){
  print("ingrese elemento de lista 2");
  lista2.add(int.parse(stdin.readLineSync()!));
}

for(int i=0;i<5;i++){
  int elemento = -25 + random.nextInt(11);
  lista3.add(elemento);
}
List<int> listaresta=[];

for(int i =0;i<5;i++){
  listaresta.add(lista[i]-lista2[i]);
}
List<int> listasuma=[];
for(int i =0;i<5;i++){
  listasuma.add(listaresta[i]+lista3[i]);
}
print("$lista  lista1");
print("$lista2  lista2");
print("$lista3 lista 3");
print("$listaresta  lista resta(primera y segunda ) ");
print("$listasuma  lista suma(lista resultante mas la tercera)");
listasuma.insert(1, 17);
listasuma.insert(2, 24);
print("$listasuma Lista con datos agregados");
listasuma.sort();
print(listasuma.reversed);//lista invertida
}