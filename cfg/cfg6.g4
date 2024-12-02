grammar cfg6;
s : s4;
s1 : 'a' s3;
s3 : 'b' | 'c';
s4 : EOF | s1 s4;
