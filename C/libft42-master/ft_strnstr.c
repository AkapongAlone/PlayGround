/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: awanngre <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/12 23:00:04 by awanngre          #+#    #+#             */
/*   Updated: 2022/06/17 15:31:08 by awanngre         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include"libft.h"

char	*ft_strnstr(const char *haystack, const char *needle, size_t len)
{
	size_t	i;
	size_t	j;

	if (len < 0)
		len *= -1;
	if (haystack[0] == 0 && needle[0] == 0)
		return ((char *)(haystack));
	j = ft_strlen(needle);
	i = 0;
	while (i < len && haystack[0] != 0)
	{
		if (haystack[0] == needle[0] && ft_strncmp(haystack, needle, j) == 0)
		{
			if (i == len -1 && j > 1)
				return (NULL);
			return ((char *)(haystack));
		}
		i++;
		haystack++ ;
	}
	return (NULL);
}		
