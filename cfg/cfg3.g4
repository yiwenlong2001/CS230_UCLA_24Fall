grammar cfg3;
s : 'a' s3 'd';
s1 : 'b' | 'c';
s3 : EOF | s1 s3;
