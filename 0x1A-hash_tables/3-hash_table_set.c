#include "hash_tables.h"

int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	hash_node_t *item = (hash_node_t *)malloc(sizeof(hash_node_t));
	unsigned long int index = key_index((const unsigned char*)key, 1024);

	ht->size = 1024;
	item->key = (char *)malloc(strlen(key) + 1);
	item->value = (char *)malloc(strlen(value) + 1);
	strcpy(item->key, key);
	strcpy(item->value, value);

	if (!ht->array[index])
	{
		ht->array[index] = item;
		return (1);
	}
	else
	{
		free(ht->array[index]->key);
		free(ht->array[index]->value);
		free(ht->array[index]);
		ht->array[index] = NULL;
		ht->array[index] = item;
		return (1);
	}
	return (0);
}
