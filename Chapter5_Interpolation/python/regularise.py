
import numpy as np

def regularise(x_full,y_full,w=None,wsd=0.005,order=2):
  '''
  An optimal interpolator / smoother

  1D only and not efficient in this implementation

  p.lewis@ucl.ac.uk
  '''
  if w == None:
    w = np.ones_like(x_full)
  w_full = w
 
  I = np.matrix(np.eye(y_full.shape[0]))
  D = (I - np.roll(I,-1)).T
  D2 = (D.T * D) ** order
  gamma = 1./(wsd**2)
  M = np.matrix(np.diag(w_full) + gamma * D2)
  V = np.matrix(w_full * y_full)
  MI = M.I
  P = np.array(V * MI).flatten() 
  uncert = np.array(np.diag(MI)).flatten()

  return P,np.sqrt(uncert)
