/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: awanngre <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/23 13:16:54 by awanngre          #+#    #+#             */
/*   Updated: 2022/06/23 16:08:43 by awanngre         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_swap(char *s, int i, int j)
{
	int	k;
	char	head;

	k = 0;
	if (j)
	{
		s[i] = '-';
		i++ ;
	}
	while (k < i / 2)
	{
		head = s[k];
		s[k] = s[i - k];
		s[i - k] = head;
		k++ ;
	}
	s[i] = 0;
}

int	ft_digit(int n)
{
	int	i;

	i = 0;
	while (n)
	{
		n /= 10;
		i++ ;
	}
	return (i);
}

char	*ft_itoa(int n)
{
	char	*ans;
	int		i;
	int		j;

	j = 0;
	if (n < 0)
		j = 1;
	ans = (char *)(malloc(sizeof(char) * ((ft_digit(n)) + j)));
	if (!(ans))
		return (NULL);
	i = 0;
	while (n)
	{
		ans[i] = (n % 10) + 48;
		n /= 10;
		i++ ;
	}
	ft_swap(ans, i, j);
	return (ans);
}
		
