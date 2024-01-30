def foo(bar, baz):
  #print ('hello {0}'.format(bar))
  return baz + " "+ bar

from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)

async_result = pool.apply_async(foo, ('world','crazy')) # tuple of args for foo

# do some other stuff in the main process
return_val = async_result.get()  # get the return value from your function.
print(return_val)