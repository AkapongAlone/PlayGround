/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: awanngre <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/20 14:29:51 by awanngre          #+#    #+#             */
/*   Updated: 2022/06/24 15:17:34 by awanngre         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void    ft_free(char **split, int len);

int	find_end(char const *s, char c)
{
	size_t	i;
	int	num;
	size_t	check;

	i = 0;
	check = 0;
	num = 0;
	while (i < ft_strlen(s))
	{
		if (s[i] == c && s[i + 1] != c)
		{
			i++ ;
			num ++;
			continue ;
		}
		check++ ;
		i++ ;
	}
	if (i == check)
		return (2);
	return (num + 1);
}

char	*create_char(char const *s,int start, int end, char **split, int len)
{
	char	*str;
	int		i;

	i = 0;
	str = (char *)(malloc(sizeof(char) * (end - start)));
	if (!(str))
		ft_free(split, len);
	while (start < end)
		str[i++] = s[start++];
	str[i] = 0;
	return (str);
}

void	ft_free(char **split, int len)
{
	int	i = 0;

	if (!(split))
		return ;
	while (i <= len)
	{
		free(split[i]);
		i++ ;
	}
	free(split);
	return ;
}

char	**ft_split(char const *s, char c)
{
	char	**split;
	size_t		i;
	int		j;
	int		start;
	int		check_char;

	check_char = 0;
	i = 0;
	j = 0;
	start = 0;
	split = (char **)(ft_calloc(sizeof(char *), (find_end(s, c))));
	if (!(split))
		return (NULL);
	while (i < ft_strlen(s))
	{
		if (s[i] != c)
			check_char = 1;
		else if ((s[i] == c || i == ft_strlen(s)) && check_char == 1)
		{
			split[j++] = create_char(s, start, i, split, find_end(s, c));
			check_char = 0;
			start = i + 1;
		}
		else
			start = i + 1;
		i++ ;
	}
	if (split[0] == 0 && check_char != 0)
		split[0] = create_char(s, 0, ft_strlen(s), split, find_end(s, c));
	return (split);
}
