def merge(A):
 if(len(A)<=1):return A;
 Left=merge(A[:len(A)//2]);Right=merge(A[len(A)//2:]);Out=[];
 while(Left)and(Right):
  if(Left[0]<Right[0]):Out.append(Left.pop(0));
  else:Out.append(Right.pop(0));
 Out.extend(Left);Out.extend(Right);return Out;
print(merge([1,4,13,1,4,5,1344,124,-13]))
