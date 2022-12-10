/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: awanngre <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/15 22:11:08 by awanngre          #+#    #+#             */
/*   Updated: 2022/06/16 01:15:12 by awanngre         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_atoi(const char *str)
{
	int	i;
	int	ans;
	int	is_neg;

	is_neg = 1;
	i = 0;
	while (!(ft_isprint(str[i])))
		i++ ;
	if (str[i] == '-')
	{
		is_neg = -1;
		i++ ;
	}
	else if (str[i] == '+')
		i++ ;
	ans = 0;
	while (1)
	{
		if (ft_isdigit(str[i]))
			ans = ans * 10 + (str[i] - 48);
		else
			return (ans * is_neg);
		i++ ;
	}
}
