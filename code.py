import display
import gc
import initialisation
import supervisor
import display

initialisation.init_system()

timer_2 = supervisor.ticks_ms()

while True:
    time_now = supervisor.ticks_ms()

    if time_now - timer_2 > 5000:
        display.show_main_menu("next")
        timer_2 = supervisor.ticks_ms()
        print(gc.mem_free())
        gc.collect()