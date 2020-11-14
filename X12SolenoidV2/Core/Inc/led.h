/*
 * led.h
 *
 *  Created on: Nov 14, 2020
 *      Author: Conne
 */

#ifndef INC_LED_H_
#define INC_LED_H_

#include "stm32f0xx_hal.h"
#include "stm32f0xx_hal_tim.h"

typedef enum TIM_FREQ
{
	TIM_FREQ_1HZ,
	TIM_FREQ_2HZ,
	TIM_FREQ_4HZ,
	TIM_FREQ_8HZ,
	TIM_FREQ_16HZ,
	TIM_FREQ_32HZ
} TimerFrequency;

void InitializeTimer(TIM_TypeDef* timerModule);
void flashLed(TimerFrequency timerFrequency);

#endif /* INC_LED_H_ */
