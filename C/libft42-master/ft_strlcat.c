/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: awanngre <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/11 12:36:59 by awanngre          #+#    #+#             */
/*   Updated: 2022/06/17 15:11:49 by awanngre         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t dstsize)
{
	size_t	i;
	size_t	j;
	size_t	k;

	i = 0;
	j = 0;
	k = 0;
	while (src[k] != 0)
		k++;
	while (dst[j] != 0)
		j++ ;
	if (dstsize <= j)
		return (dstsize + k);
	while (i < dstsize - j - 1 && src[i] != 0)
	{
		dst[j + i] = src[i];
		i++ ;
	}
	dst[j + i] = 0;
	return (j + k);
}
