#include "hash_tables.h"

/**
* key_index - A function that returns the index of a key.
* @key: The key
* @size: The size of the array
*
* Return: The index of the key
*/

unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	unsigned long int index = hash_djb2(key);

	return (index % size);
}
