grammar cfg20;
s : s4;
s1 : '1' | '2' | '3';
s4 : s1 | s1 s4;

WS : [ \t\r\n]+ -> skip ;