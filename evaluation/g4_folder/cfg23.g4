grammar cfg23;
s : s1;
s1 :   | 'a' s1;

WS : [ \t\r\n]+ -> skip ;