# -*- coding:utf-8 -*-
# 快速排序
def quicksort(arr,l,r):
	if l<r:
		i,j = l,r
		x = arr[i]
		while i <j:
			while i < j and arr[j]>=x:
				j-=1
			if i<j:
				arr[i] = arr[j]
				i+=1
			while i<j and arr[i]<=x :
				i+=1
			if i<j:
				arr[j] = arr[i]
				j-=1
		arr[i] = x
		quicksort(arr,l,i-1)
		quicksort(arr,i+1,r)
	print arr


# 直接插入排序
def insertsort(arr):
	n = len(arr)
	for i in range(0,n):
		if arr[i-1]>arr[i]:
			temp = arr[i]
			j = i - 1
			while j>=0 and arr[j]>temp:
				arr[j+1] = arr[j]
				j-=1
			arr[j+1]=temp
	print arr


# 删除列表内重复的元素
def deleterepetition(arr):
	arr1 = []
	for item in arr:
		if not item in arr1:
			arr1.append(item)
	print arr1


#直接选择排序
def selectsort(arr):
	n = len(arr)
	for i in range(0,n):
		mina = arr[i]
		for j in range(i+1,n):
			if arr[j]<mina:
				mina = arr[j]
		c = arr[i]
		arr[i] = mina
		mina = c
	print arr


# 冒泡排序
def BubbleSort(arr):
	n = len(arr)
	flag = n
	while flag>0:
		k = flag
		flag = 0
		for j in range(1,k):
			if arr[j-1]>arr[j]:
				temp = arr[j-1]
				arr[j-1] = arr[j]
				arr[j] = temp
				flag = j
	print arr


# 希尔排序
def shellsort(arr):
	n = len(arr)
	gap = n/2
	while gap>0:
		for i in range(gap,n):
			j= i - gap
			while j>=0 and arr[j]>arr[j+gap]:
				temp = arr[j]
				arr[j] = arr[j+gap]
				arr[j+gap] = temp
				j -= gap
		gap = gap/2
	print arr


# 归并排序
def mergearry(arr,first,mid,last,temp):
	i,j,m,n,k = first,mid+1,mid,last,0
	temp = []
	while i<=m and j<=n:
		if a[i]<=a[j]:
			temp[k] = a[i]
			k += 1
			i += 1
		else:
			temp[k] = a[j]
			k += 1
			j += 1
	while i<=m:
		temp[k] = a[i]
		k += 1
		i += 1
	while j<=n:
		temp[k] = a[j]
		k += 1
		j += 1
	for i in range(0,k):
		a[first+i] = temp[i]

def mergesort(arr,first,last,temp):
	if first<last:
		mid = (first + last)/2
		mergesort(a,first,mid,temp)
		mergesort(a,mid+1,last,temp)
		mergearry(a,first,mid,last,temp)
	print arr














	




				
			

	