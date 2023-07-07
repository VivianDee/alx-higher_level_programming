#include "hash_tables.h"

/**
* hash_table_delete - A function that deletes a hash table.
* @ht: The hash table
*
*/

void hash_table_delete(hash_table_t *ht)
{
	unsigned long int i;

	for (i = 0; i < ht->size; i++)
	{
		if (ht->array[i])
		{
			free(ht->array[i]->key);
			free(ht->array[i]->value);
			free(ht->array[i]);
		}
	}

	free(ht->array);
	free(ht);
}
