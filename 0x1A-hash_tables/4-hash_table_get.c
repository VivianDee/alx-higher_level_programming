#include "hash_tables.h"

/**
* hash_table_get - A function that retrieves a value associated with a key.
* @ht: The hash table
* @key: The key
*
* Return:
* - The value associated with the key
* - NULL
*/

char *hash_table_get(const hash_table_t *ht, const char *key)
{
	unsigned long int index = key_index((const unsigned char *)key, ht->size);
	hash_node_t *item = NULL;

	item = ht->array[index];
	if (item)
	{
		if (strcmp(item->key, key) == 0)
			return (item->value);
	}

	return (NULL);
}
