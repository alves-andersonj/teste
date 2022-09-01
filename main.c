#include <stdio.h>
int main()
{
    int i;
    i=0;
    
    for (i = 1; i <= 100; ++i)
    {
		if (i % 3 == 0)
			printf("%s\n","Foo");
		else if (i % 5 == 0)
			printf("%s\n","Baa");
		else if (i % 15 == 0)
			printf("%s\n","FooBaa");
		else 
			printf("%d\n",i);
	}
}
