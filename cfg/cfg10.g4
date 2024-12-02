grammar cfg10;
s : 'a' s2;
s1 : 'b' 'c';
s2 : EOF | s1;
