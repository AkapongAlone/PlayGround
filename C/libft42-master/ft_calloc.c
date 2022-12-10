/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: awanngre <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/16 16:31:31 by awanngre          #+#    #+#             */
/*   Updated: 2022/06/22 20:20:14 by awanngre         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t count, size_t size)
{
	char	*ans;
	size_t	i;

	i = 0;
	ans = (char *)(malloc(count * size));
	if (size >= SIZE_MAX)
		return (NULL);
	if (!(ans))
		return (NULL);
	while (i < count * size)
	{
		ans[i] = 0;
		i++ ;
	}
	//ft_bzero(ans, size);
	return (ans);
}
