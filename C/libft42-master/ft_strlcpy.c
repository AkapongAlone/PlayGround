/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: awanngre <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/11 00:04:44 by awanngre          #+#    #+#             */
/*   Updated: 2022/06/12 23:25:53 by awanngre         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t
	ft_strlcpy(char *dst, const char *src, size_t dstsize)
{
	size_t	i;
	size_t	j;

	i = 0;
	j = 0;
	while (src[j] != 0)
		j++ ;
	if (dstsize == 0)
		return (j);
	while (i < dstsize - 1 && src[i] != 0)
	{
		dst[i] = src[i];
		i++ ;
	}
	dst[i] = 0;
	return (j);
}
