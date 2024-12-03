grammar cfg9;
s : 'a' s2;
s1 : 'b' 'c';
s2 : EOF | s1;

WS : [ \t\r\n]+ -> skip ;