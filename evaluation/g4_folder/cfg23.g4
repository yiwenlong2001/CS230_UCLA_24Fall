grammar cfg23;
s : s1;
s1 : '0' | '1' | '2' | '3' | 'a' | 'b' | 'c' | 'd';

WS : [ \t\r\n]+ -> skip ;