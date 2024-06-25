package Prova.Prova_09_08.java;

import java.util.Hashtable;
import java.util.Random;

import javax.jms.*;
import javax.naming.*;


public class Client {
    
    public static void main(String[] args) {
        
        Hashtable<String, String>proprieties = new Hashtable<String, String>();
        proprieties.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        proprieties.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        //aggiungere alle proprietà i nomi delle code fisiche
        proprieties.put("topic.data", "mydata");

        try {
            //Creo il contesto iniziale con le proprietà
            Context jndiContext = new  InitialContext(proprieties);

            //Faccio il lookup al context
            TopicConnectionFactory connectionFactory = (TopicConnectionFactory) jndiContext.lookup("TopicConnectionFactory");
            Topic topic = (Topic) jndiContext.lookup("data");

            TopicConnection topiConnection = connectionFactory.createTopicConnection();
            TopicSession topicSession = topiConnection.createTopicSession(false, 0);
            TopicPublisher publisher =  topicSession.createPublisher(topic);
        
            MapMessage mapMessage = topicSession.createMapMessage();

            String tipo;

            if (args[0].equalsIgnoreCase("temperature")){
                tipo = "temperature";
            } else if (args[0].equalsIgnoreCase("pressure")){
                tipo = "pressure";
            }else {
                System.err.println("Tipo non valido");
                return;
            }
            Random rand = new Random();

            
            for (int i  = 0; i < 20 ; i++) {
                
                mapMessage.setString("type", tipo);
            

                if (tipo.equals("temperature")){
                
                    mapMessage.setInt("type", rand.nextInt(0,101));

                }
                else {
                
                    mapMessage.setInt("type", rand.nextInt(1000,1051));

                }
                publisher.send(mapMessage);
            }

            publisher.close();
            topicSession.close();
            topiConnection.close();
            

        } catch (NamingException e) {
        
            System.out.println("[CLIENT] NamingException: "+ e);
        } catch (JMSException e) {
            System.out.println("[CLIENT] JMSExceptio: " +e);
        
        }

    }

}
