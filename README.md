# TymeBox
lightweight CLI application to manage and plan daily tasks while tracking long-term accomplishment


# user commands 

## allocate and re-allocate 
tymebox allocate data-science 3:00 daily
tymebox allocate diffeq 1:25 m,w,s,u

## remove 
tymebox remove data-science

-----------------------------------------------------------

## start task
tymebox start diffeq "hw.1 1-20" :30
tymebox start data-science -> bishop "implement poly reg" 1:30

tymebox start bishop "regularization" :25   

## pause and resume
tymebox pause
tymebox resume 

## view task status and progress in real-time
tymebox status
tymebox close

## on task end
tymebox complete  (or simply start a new task at any time)
tymebox extend :15
tymebox defer  

-----------------------------------------------------------

## Track long term progress
tymebox today

tymebox progress --week
tymebox progress --total


