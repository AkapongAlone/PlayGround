/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: awanngre <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/02 14:09:50 by awanngre          #+#    #+#             */
/*   Updated: 2022/06/19 09:49:58 by awanngre         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include"libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*str;
	size_t	i;
	size_t	j;
	unsigned int	k;

	i = 0;
	j = ft_strlen(s + start);
	k = ft_strlen(s);
	if (j < len)
		str = (char *)(malloc(sizeof(char) * (j)));
	else
		str = (char *)(malloc(sizeof(char) * (len)));
	if (!str)
		return (NULL);
	while (s[start + i] != 0 && i < len && k > start)
	{
		str[i] = s[start + i];
		i++ ;
	}
	str[i] = 0;
	return (str);
}
