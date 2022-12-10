/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: awanngre <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/02 20:44:28 by awanngre          #+#    #+#             */
/*   Updated: 2022/06/19 22:39:10 by awanngre         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include"libft.h"

int	isinset(char s1, char const *set)
{
	int	j;

	j = 0;
	while (set[j] != 0)
	{
		if (s1 == set[j])
			return (1);
		j ++;
	}
	return (0);
}

int	len_ans(char const *s1, char const *set)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	while (s1[j] != 0)
	{
		if (isinset(s1[j], set))
		{
			j++ ;
			continue ;
		}
		i++ ;
		j++ ;
	}
	return (i);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*str;
	int		i;
	int		j;
	int		k;

	j = 0;
	i = 0;
	k = len_ans(s1, set);
	str = (char *)(malloc(sizeof(char) * k));
	if (!(str))
		return (NULL);
	while (s1[j] != 0)
	{
		if (isinset(s1[j], set))
		{
			j++ ;
			continue ;
		}
		str[i] = s1[j];
		i++ ;
		j++ ;
	}
	str[i] = 0;
	return (str);
}
