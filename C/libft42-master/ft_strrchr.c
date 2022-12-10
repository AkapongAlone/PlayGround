/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: awanngre <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/09 23:50:11 by awanngre          #+#    #+#             */
/*   Updated: 2022/06/12 23:26:57 by awanngre         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int	i;

	i = -1;
	if (c > 256)
		c -= 256 ;
	while (s[++i] != 0)
		continue ;
	while (i >= 0)
	{	
		if (s[i] == c)
			return ((char *)(s + i));
		i-- ;
	}
	return (NULL);
}
