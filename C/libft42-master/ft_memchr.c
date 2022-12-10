/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: awanngre <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/08 22:13:44 by awanngre          #+#    #+#             */
/*   Updated: 2022/06/17 16:14:32 by awanngre         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t	i;

	i = 0;
	if (c > 256)
		c = c - 256;
	while (i < n)
	{
		if (*(unsigned char *)(s + i) == c)
			return ((unsigned char *)(s + i));
		i++ ;
	}
	return (NULL);
}
