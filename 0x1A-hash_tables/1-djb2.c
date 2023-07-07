#include "hash_tables.h"

/**
* hash_djb2 - A hash function implementing the djb2 algorithm
* @str: The key
*
* Return: The generated hash
*/

unsigned long int hash_djb2(const unsigned char *str)
{
	unsigned long int i;
	int num;

	i = 5381;
	while ((num = *str++))
	{
		i = ((i << 5) + i) + num;
	}

	return (i);
}
