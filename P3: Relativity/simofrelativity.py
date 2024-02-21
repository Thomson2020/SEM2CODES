import matplotlib.pyplot as plt
import numpy as np

def lorentz_transform(x, t, v, c=299792458):
    gamma = 1 / np.sqrt(1 - (v/c)**2)
    x_prime = gamma * (x - v * t)
    t_prime = gamma * (t - v * x / c**2)
    return x_prime, t_prime

def world_line(v, u, relative_v, c=299792458):
    # Time limits
    t_min = -10
    t_max = 10

    # Calculate particle positions in K' frame
    x_kprime, t_kprime = lorentz_transform(0, 0, relative_v)
    u_kprime = lorentz_transform(u, 0, relative_v)[0]

    # Calculate particle positions in K frame
    x_k, t_k = lorentz_transform(x_kprime, t_kprime, -relative_v)
    u_k = lorentz_transform(u_kprime, 0, -relative_v)[0]

    # Calculate event positions in K' frame
    x_event_kprime, t_event_kprime = lorentz_transform(0, -t_min, relative_v)
    x_event2_kprime, t_event2_kprime = lorentz_transform(0, t_max, relative_v)

    # Calculate event positions in K frame
    x_event_k, t_event_k = lorentz_transform(x_event_kprime, t_event_kprime, -relative_v)
    x_event2_k, t_event2_k = lorentz_transform(x_event2_kprime, t_event2_kprime, -relative_v)

    # Plot both frames in subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Plot K frame
    ax1.set_xlabel("ct (m)")
    ax1.set_ylabel("x (m)")
    ax1.set_title("World Lines in K Frame")

    ax1.plot(c * t_k, x_k, label="Particle")
    ax1.plot(c * t_k, u_k, label="Event")
    ax1.plot([c * t_event_k, c * t_event2_k], [x_event_k, x_event2_k], label="Light Cone")
    ax1.legend()

    # Plot K' frame
    ax2.set_xlabel("ct' (m)")
    ax2.set_ylabel("x' (m)")
    ax2.set_title("World Lines in K' Frame")

    ax2.plot(c * t_kprime, x_kprime, label="Particle")
    ax2.plot(c * t_kprime, u_kprime, label="Event")
    ax2.plot([c * t_event_kprime, c * t_event2_kprime], [x_event_kprime, x_event2_kprime], label="Light Cone")
    ax2.legend()

    plt.show()

# Test with basic values
world_line(0.8 * 299792458, 0.5 * 299792458, 0.2 * 299792458)

