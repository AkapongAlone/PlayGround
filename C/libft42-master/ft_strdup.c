/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: awanngre <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/17 15:15:51 by awanngre          #+#    #+#             */
/*   Updated: 2022/06/17 15:28:36 by awanngre         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s1)
{
	int	i;
	int	j;
	char	*str;

	i = ft_strlen(s1);
	j = 0;
	str = (char *)(malloc(sizeof(char) * i));
	if (!(s1))
		return (NULL);
	if (j == i)
		str[j] = s1[j];
	while (j < i)
	{
		str[j] = s1[j];
		j++ ;
	}
	return (str);
}
