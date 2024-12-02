grammar cfg16;
s : s1;
s1 : 'b' s2;
s2 : 'b' s3;
s3 : 'b' s3 | EOF;
